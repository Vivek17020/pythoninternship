
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "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"  
    OPENAI_KEY = 'enter-openai-api-key-here'    
config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
