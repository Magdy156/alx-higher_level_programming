-- Lists all shows in hbtn_0d_tvshows that have at least one genre linked.
SELECT sh.`title`, g.`genre_id`
FROM `tv_shows` AS sh
INNER JOIN `tv_show_genres` AS g
ON sh.`id` = g.`show_id`
ORDER BY sh.`title`, g.`genre_id`;
