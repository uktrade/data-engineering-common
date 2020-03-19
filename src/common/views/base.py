from flask import current_app as flask_app
from flask import request
from flask.views import View

from common.api.utils import to_web_dict


class PaginatedListView(View):
    def dispatch_request(self):
        orientation = request.args.get('orientation', 'tabular')
        pagination_size = flask_app.config['app']['pagination_size']
        next_id = request.args.get('next-id')

        where = ''
        values = []

        if next_id is not None:
            where = 'where id >= %s'
            values = [next_id]

        sql_query = f'''
            select id, {','.join(
                [field for field, _ in self.pipeline._l1_data_column_types]
            )}
            from {self.model.get_fq_table_name()}
            {where}
            order by id
            limit {pagination_size} + 1
        '''

        df = flask_app.dbi.execute_query(sql_query, data=values, df=True)
        if len(df) == pagination_size + 1:
            next_ = '{}{}?'.format(request.host_url[:-1], request.path)
            next_ += 'orientation={}'.format(orientation)
            next_ += '&next-id={}'.format(df['id'].values[-1])
            df = df[:-1]
        else:
            next_ = None
        web_dict = to_web_dict(df.iloc[:, 1:], orientation)
        web_dict['next'] = next_
        return flask_app.make_response(web_dict)
