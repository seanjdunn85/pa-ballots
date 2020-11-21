CREATE DATABASE `pa_general` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */;
CREATE TABLE `mail_in_ballots` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `County Name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Applicant Party Designation` varchar(45) DEFAULT NULL,
  `Date of Birth` date DEFAULT NULL,
  `Mail Application Type` varchar(45) DEFAULT NULL,
  `Application Request Date` datetime DEFAULT NULL,
  `Application Approved Date` datetime DEFAULT NULL,
  `Ballot Mailed Date` datetime DEFAULT NULL,
  `Ballot Returned Date` datetime DEFAULT NULL,
  `State House District` varchar(255) DEFAULT NULL,
  `State Senate District` varchar(255) DEFAULT NULL,
  `Congressional District` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1821325 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
