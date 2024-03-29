-- Lists all shows in the database hbtn_0d_tvshows without a genre linked.
-- 
SELECT sh.`title`, g.`genre_id`
FROM `tv_shows` AS sh
LEFT JOIN `tv_show_genres` AS g
ON sh.`id` = g.`show_id`
WHERE g.`genre_id` IS NULL
ORDER BY sh.`title`, g.`genre_id`;
