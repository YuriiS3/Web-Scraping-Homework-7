import sqlite3


class QuotesPipeline:
    def open_spider(self, spider):
        self.connection = sqlite3.connect("Authors_Quotes.db")
        self.cursor = self.connection.cursor()
        sql = """
            create table if not exists [Authors_Quotes] (
                [text] text,
                [author] text
            )
        """
        self.cursor.execute(sql)

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        self.cursor.execute(
            "insert into [Authors_Quotes] ([text], [author]) values (?, ?)",
            (item['text'], item['author'])
        )
        self.connection.commit()
        return item
