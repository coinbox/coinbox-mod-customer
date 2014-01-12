import cbpos
from cbpos.modules import BaseModuleMetadata

class ModuleMetadata(BaseModuleMetadata):
    base_name = 'customer'
    version = '0.1.0'
    display_name = 'Customer and Customer Groups'
    dependencies = (
        ('base', '0.1'),
        ('currency', '0.1')
    )
    config_defaults = tuple()
