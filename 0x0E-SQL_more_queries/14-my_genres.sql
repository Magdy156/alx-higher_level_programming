-- lists all Comedy shows in the database hbtn_0d_tvshows
SELECT g.`name` FROM `tv_genres` AS g
INNER JOIN `tv_show_genres` AS sh
ON g.`id` = sh.`genre_id`
INNER JOIN `tv_shows` AS t
ON t.`id` = sh.`show_id`
WHERE t.`title` = "Dexter"
ORDER BY g.`name`;
