SELECT * FROM supplyusapi_packagetype

DELETE From auth_user
Where id=6

Delete from authtoken_token where user_id=6

SELECT "supplyusapi_classlistsupplyitem"."id", "supplyusapi_classlistsupplyitem"."class_list_id", "supplyusapi_classlistsupplyitem"."supply_item_id", "supplyusapi_classlistsupplyitem"."number", "supplyusapi_classlistsupplyitem"."description", "supplyusapi_classlistsupplyitem"."package_type_id" FROM "supplyusapi_classlistsupplyitem" INNER JOIN "supplyusapi_classlist" ON ("supplyusapi_classlistsupplyitem"."class_list_id" = "supplyusapi_classlist"."id") INNER JOIN "supplyusapi_userclass" ON ("supplyusapi_classlist"."id" = "supplyusapi_userclass"."class_list_id") WHERE "supplyusapi_userclass"."user_id" = 2