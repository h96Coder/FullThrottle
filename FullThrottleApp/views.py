from django.views.generic import View
from django.http import HttpResponse
import json
from FullThrottleApp.models import User, ActivityPeriod
from FullThrottleApp.mixins import SerializeMixin


class fullthrottleview(View, SerializeMixin):
    def get(self, request, *args, **kwargs):
        qs_user = User.objects.all()
        json_data = self.serialize_user(qs_user)
        dict_user = json.loads(json_data)
        final_dict = dict_user
        for user in dict_user:
            qs_activity = ActivityPeriod.objects.exclude(['start_time', 'end_time']).all().filter(
                user_id=user.get('id'))
            json_data = self.serialize_activity(qs_activity)
            print(json_data)
            temp_dict = json.loads(json_data)
            user['activity_periods'] = temp_dict
        final_dict = {"ok": True, "members": final_dict}
        return HttpResponse(json.dumps(final_dict), content_type="application/json")
