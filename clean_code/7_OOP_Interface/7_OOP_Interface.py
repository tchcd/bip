
1.
class User:
    def __init__(self):
        """
        Здесь мог бы быть if user_type == advertiser
        тогда логика создания юзера релкамодателя,
        если вебмастер то логика создания веюмастера.
        Но лучше сделать фабричные методы
        """
        pass

    @staticmethod
    def create_advertiser(name, adv):
        pass

    @staticmethod
    def create_webmaster(name, site):
        pass


2.
class MarketingCampaign:
    def __init__(self, name, start_date, end_date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date

    @staticmethod
    def create_youtube_campaign(name, start_date, end_date):
        print('Создал Ютуб кампанию')
        return MarketingCampaign(name, start_date, end_date)

    @staticmethod
    def create_vk_campaign(name, start_date, end_date):
        print('Создал ВК кампанию')
        return MarketingCampaign(name, start_date, end_date)

    def run(self):
        return


camp = MarketingCampaign.create_youtube_campaign('test_youtube_campaign', '2023-01-01', '2023-12-31')
camp.run()



3.
class DatabaseConnector:
    def __init__(self, dsn):
        self.dsn = dsn

    def create_connection(self):
        pass

class MysqlConnector(DatabaseConnector):
    def create_connection(self):
        return 'mysql.connector.connect(self.dsn)'


class PostgresConnector(DatabaseConnector):
    def create_connection(self):
        return 'psycopg.connect(self.dsn)'


class DatabaseConnectorImp:
    def __init__(self, connector: DatabaseConnector):
        self.connector = connector

    def create_connection(self):
        return self.connector.create_connection()


connect = DatabaseConnectorImp(
    PostgresConnector(
        "user=user password=password host=127.0.0.1 database=public"
    )
).create_connection()
