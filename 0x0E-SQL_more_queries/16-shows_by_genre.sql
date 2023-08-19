-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
SELECT t.`title`, g.`name` FROM `tv_shows` AS t
LEFT JOIN `tv_show_genres` AS sh
ON t.`id` = sh.`show_id`
LEFT JOIN `tv_genres` AS g
ON sh.`genre_id` = g.`id`
ORDER BY t.`title`, g.`name`;
