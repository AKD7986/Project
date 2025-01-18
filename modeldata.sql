-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 16, 2024 at 01:02 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `modeldata`
--

-- --------------------------------------------------------

--
-- Table structure for table `form_column`
--

CREATE TABLE `form_column` (
  `bedrooms` int(11) NOT NULL,
  `bathrooms` float NOT NULL,
  `lvarea` bigint(15) NOT NULL,
  `loarea` bigint(20) NOT NULL,
  `floors` float NOT NULL,
  `waterfront` varchar(50) NOT NULL,
  `house_condition` varchar(50) NOT NULL,
  `grade` int(20) NOT NULL,
  `house_area_base` bigint(20) NOT NULL,
  `base_area` bigint(20) NOT NULL,
  `built_year` bigint(20) NOT NULL,
  `renew_year` bigint(20) NOT NULL,
  `code` bigint(20) NOT NULL,
  `lvrenew` bigint(20) NOT NULL,
  `lorenew` bigint(20) NOT NULL,
  `schools` int(10) NOT NULL,
  `price` bigint(50) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `form_column`
--

INSERT INTO `form_column` (`bedrooms`, `bathrooms`, `lvarea`, `loarea`, `floors`, `waterfront`, `house_condition`, `grade`, `house_area_base`, `base_area`, `built_year`, `renew_year`, `code`, `lvrenew`, `lorenew`, `schools`, `price`, `date`) VALUES
(4, 2, 2920, 4000, 1, 'No', 'Excellent', 8, 1910, 1010, 1909, 0, 122004, 2470, 4000, 2, 1190380, '2024-08-07'),
(2, 1, 3020, 6000, 1, 'Yes', 'Very Good', 4, 1700, 1500, 1950, 0, 122034, 3000, 7000, 3, 1022072, '2024-08-07'),
(3, 2, 1920, 9000, 2, 'Yes', 'Excellent', 5, 2000, 1100, 1990, 0, 122012, 3209, 9090, 1, 533635, '2024-08-07'),
(3, 2, 1920, 9000, 2, 'Yes', 'Excellent', 5, 2000, 1100, 1990, 0, 122012, 3209, 9090, 1, 533635, '2024-08-07'),
(3, 2, 1920, 9000, 2, 'Yes', 'Excellent', 5, 2000, 1100, 1990, 0, 122012, 3209, 9090, 1, 533635, '2024-08-07'),
(3, 1, 9752, 9087, 1, 'Yes', 'Good', 4, 4567, 9876, 2010, 0, 122056, 7890, 8000, 2, 2014075, '2024-08-07'),
(4, 2, 2920, 4000, 1, 'No', 'Excellent', 8, 1910, 1010, 1909, 0, 122004, 2470, 4000, 2, 1190380, '2024-08-07'),
(12, 2, 2920, 4000, 3, 'No', 'Excellent', 5, 1910, 1010, 1900, 0, 122004, 2470, 4000, 1, 742110, '2024-08-07'),
(1, 1, 900, 8900, 1, 'No', 'Excellent', 8, 345, 567, 2000, 4561, 122044, 24701, 4000, 2, 743945, '2024-08-07'),
(1, 1, 900, 8900, 1, 'No', 'Excellent', 8, 345, 567, 2000, 4561, 122044, 24701, 4000, 2, 743945, '2024-08-07'),
(4, 2, 2920, 4000, 1, 'No', 'Excellent', 8, 1910, 1010, 1909, 1949, 122004, 2470, 4000, 2, 1190580, '2024-08-07'),
(2, 1, 13232, 4000, 1, 'Yes', 'Excellent', 5, 1988, 1010, 1909, 0, 122072, 2470, 4000, 2, 2041854, '2024-08-07'),
(2, 1, 1323, 7543, 1, 'Yes', 'Very Good', 6, 6543, 543, 2012, 2014, 122033, 6000, 76543, 1, 453417, '2024-08-07'),
(3, 2, 1680, 7000, 1, 'Yes', 'Excellent', 7, 1680, 0, 1968, 0, 122072, 1540, 7480, 3, 418031, '2024-08-07'),
(5, 2, 1680, 7000, 2, 'No', 'Excellent', 7, 1680, 3456, 1968, 0, 122072, 1540, 7480, 3, 239596, '2024-08-07'),
(4, 2, 1680, 2300, 2, 'Yes', 'Good', 5, 1680, 0, 1968, 0, 122054, 1654, 7654, 2, 519628, '2024-08-10'),
(5, 2, 5433, 7000, 2, 'No', 'Good', 6, 5433, 4322, 1966, 0, 122023, 1222, 3433, 2, 1060164, '2024-08-11'),
(4, 2, 2322, 1111, 2, 'No', 'Very Good', 5, 3322, 1231, 1970, 0, 122046, 2322, 2200, 2, 467464, '2024-08-12'),
(3, 2, 1680, 7000, 1, 'No', 'Excellent', 7, 1222, 0, 1968, 0, 122072, 1540, 7480, 1, 236568, '2024-08-16'),
(3, 1, 900, 2300, 1, 'Yes', 'Very Good', 6, 9099, 0, 1988, 1999, 122022, 1220, 2280, 2, 273286, '2024-08-16'),
(4, 2, 1680, 7000, 1, 'Yes', 'Excellent', 6, 1680, 1232, 1990, 0, 122045, 1220, 7480, 2, 481466, '2024-08-16');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
