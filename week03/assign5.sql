-- 使用 MySQL 官方文档，学习通过 sql 语句为上题中的 id 和 name 增加索引，并验证。根据执行时间，增加索引以后是否查询速度会增加？请论述原因，并思考什么样的场景下增加索引才有效。

ALTER TABLE `table_name` ADD INDEX index_name ( `name` )

ALTER TABLE `table_name` ADD INDEX index_id ( `id` ) 

-- 雖然索引大大提高了查詢速度，同時卻會降低更新表的速度，如對表進行INSERT、UPDATE和DELETE。
-- 因為更新表時，MySQL不僅要儲存資料，還要儲存一下索引檔案。
-- 建立索引會佔用磁碟空間的索引檔案。
-- 如果你在一個大表上建立了多種組合索引，索引檔案的會膨脹很快。
-- 索引只是提高效率的一個因素，如果你的MySQL有大資料量的表，就需要花時間研究建立最優秀的索引，或優化查詢語句。