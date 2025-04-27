-- 코드를 작성해주세요
select ii.item_id, item_name, rarity
from ITEM_INFO ii
left join item_tree it on ii.item_id = it.parent_item_id
where it.item_id is null
order by 1 desc;

# """
# 자식 - 부모
# 자식이 비어 있으면
# 더이상 업데이트가 안됨

# """