#
# Structure for table "poi"
#

DROP TABLE IF EXISTS 'poi';
CREATE TABLE 'poi' (
    'fid' int(11) NOT NULL DEFAULT '0',
    'name' varchar(100) NOT NULL DEFAULT '',
    'lng' decimal(10,7) DEFAULT NULL,
    'lat' float(10,6) DEFAULT NULL,
    'category' varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

#
# Data for table "poi"
#

/*!40000 ALTER TABLE 'poi' DISABLE KEYS */;
INSERT INTO 'poi' VALUES (1, 'Bus Stop', 103.6393051, 1.561018,'transport');