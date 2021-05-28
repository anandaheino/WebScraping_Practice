#!/bin/bash
NOW=$(date +"%m-%d-%y-%r" | sed 's/-//g'| sed 's/://g')
NOW=`echo $NOW | sed 's/ *$//g'`
FILE="${NOW}"

scrapy crawl easy -o siteA$FILE.csv
scrapy crawl basic -o siteB$FILE.csv
