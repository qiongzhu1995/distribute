# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.exporters import JsonLinesItemExporter


class CsdnDownFilePipeline:
    def __init__(self):
        self.csdn = open('csdn.json', 'wb')

        self.csdn_exporter = JsonLinesItemExporter(
            self.csdn, ensure_ascii=False
        )

    def process_item(self, item, spider):
        self.csdn_exporter.export_item(item)
        return item

    def close_spider(self, item, spider):
        self.csdn.close()