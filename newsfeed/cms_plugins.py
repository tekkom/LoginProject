from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from newsfeed.models import NewspiecePluginModel
from django.utils.translation import ugettext as _

class NewsfeedPluginPublisher(CMSPluginBase):
    model = NewspiecePluginModel  # model where plugin data are saved
    module = _("Newsfeed")
    name = _("Newsfeed plugin")  # name of the plugin in the interface
    render_template = "newsfeed_cms/newsfeed_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(NewsfeedPluginPublisher)  # register the plugin
