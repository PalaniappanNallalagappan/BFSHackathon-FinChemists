CREATE TABLE `emails` (
  `id` int(11) DEFAULT NULL,
  `textmessage` varchar(8000) DEFAULT NULL,
  `category` varchar(256) DEFAULT NULL,
  `date` datetime DEFAULT CURRENT_TIMESTAMP
) ;

CREATE TABLE `requests` (
  `srid` varchar(10) DEFAULT NULL,
  `textmessage` varchar(8000) DEFAULT NULL,
  `assignedto` varchar(256) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `status` varchar(44) DEFAULT NULL
) ;