-- Lists all shows contained in the database hbtn_0d_tvshows.
-- If a show doesn’t have a genre, display NULL
SELECT sh.`title`, g.`genre_id`
FROM `tv_shows` AS sh
LEFT JOIN `tv_show_genres` AS g
ON sh.`id` = g.`show_id`
ORDER BY sh.`title`, g.`genre_id`;
