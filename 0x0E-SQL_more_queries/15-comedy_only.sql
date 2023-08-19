-- lists all Comedy shows in the database hbtn_0d_tvshows
SELECT t.`title` FROM `tv_shows` AS t
INNER JOIN `tv_show_genres` AS sh
ON t.`id` = sh.`show_id`
INNER JOIN `tv_genres` AS g
ON g.`id` = sh.`genre_id`
WHERE g.`name` = "Comedy"
ORDER BY t.`title`;
