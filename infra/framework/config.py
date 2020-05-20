import inject
from core.port.persistence.branch import IBranchRepository
from infra.persistence.branch_repository import BranchRepository

class Config:
    DEBUG = False

    def config_inject(binder: inject.Binder) -> None:
        binder(IDatabase, MongoDBAdapter(db_config))
        binder.bind(IBranchRepository, BranchRepository())
    
    inject.configure(config_inject)

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    DEBUG = True

class StagingConfig(Config):
    DEBUG = False

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}