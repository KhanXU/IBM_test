select t2.owner_id, t2.owner_name, count(t3.category_id)
from `article` as t1, `owner` as t2, `category` as t3, `category_article_mapping` as t4 
on t4.category_id = t3.category_id join t4.article_id = t1.article_id join t1.owner_id = t2.owner_id
group by t2.owner_id
desc;