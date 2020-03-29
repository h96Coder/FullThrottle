from django.core.serializers import serialize
import json


class SerializeMixin(object):
    def serialize_user(self,qs):
        json_data=serialize('json',qs)
        p_data=json.loads(json_data)
        final_list=[]
        for obj in p_data:
            emp_data={'id':obj['pk']}
            data=obj['fields']
            emp_data.update(data)
            final_list.append(emp_data)
        json_data=json.dumps(final_list)
        return json_data

    def serialize_activity(self, qs):
        json_data = serialize('json', qs)
        p_data = json.loads(json_data)
        final_list = []
        for obj in p_data:
            emp_data = obj['fields']
            emp_data.pop("user_id")
            final_list.append(emp_data)
        json_data = json.dumps(final_list)
        return json_data