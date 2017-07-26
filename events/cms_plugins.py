from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from events.models import EventsPluginModel
from django.utils.translation import ugettext as _


class EventPluginPublisher(CMSPluginBase):
    model = EventsPluginModel  # model where plugin data are saved
    module = _("Events")
    name = _("Event Plugin")  # name of the plugin in the interface
    render_template = "events_cms_integration/event_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(EventPluginPublisher)  # register the plugin
