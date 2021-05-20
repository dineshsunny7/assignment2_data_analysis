-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 20, 2021 at 11:26 AM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.3.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bestdoc`
--

-- --------------------------------------------------------

--
-- Table structure for table `hospital_details`
--

CREATE TABLE `hospital_details` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `area` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hospital_details`
--

INSERT INTO `hospital_details` (`id`, `name`, `area`) VALUES
(1, 'image', 'kochi'),
(2, 'medicover', 'lingampally'),
(3, 'yashoda', 'calicut'),
(4, 'doctor.com', 'kochi'),
(5, 'my doctor', 'vizag');

-- --------------------------------------------------------

--
-- Table structure for table `hospital_rating`
--

CREATE TABLE `hospital_rating` (
  `area` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `administration` int(11) NOT NULL,
  `bd` int(11) NOT NULL,
  `doctor` int(11) NOT NULL,
  `facility` int(11) NOT NULL,
  `nursing` int(11) NOT NULL,
  `services` int(11) NOT NULL,
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hospital_rating`
--

INSERT INTO `hospital_rating` (`area`, `name`, `administration`, `bd`, `doctor`, `facility`, `nursing`, `services`, `id`) VALUES
('kochi', 'image', 105, 56, 79, 55, 54, 54, 1),
('lingampally', 'medicover', 100, 50, 100, 50, 50, 50, 2),
('calicut', 'yashoda', 125, 57, 79, 55, 54, 54, 3),
('kochi', 'doctor.com', 100, 50, 100, 50, 50, 50, 4),
('vizag', 'my doctor', 100, 50, 100, 50, 50, 50, 5);

-- --------------------------------------------------------

--
-- Table structure for table `hospital_rating_administration`
--

CREATE TABLE `hospital_rating_administration` (
  `id` int(11) NOT NULL,
  `question1` int(11) NOT NULL,
  `question2` float NOT NULL,
  `question3` float NOT NULL,
  `question4` float NOT NULL,
  `question5` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hospital_rating_administration`
--

INSERT INTO `hospital_rating_administration` (`id`, `question1`, `question2`, `question3`, `question4`, `question5`) VALUES
(5, 50, 0, 0, 0, 50),
(4, 50, 0, 0, 0, 50),
(2, 50, 0, 0, 0, 50),
(3, 60, 1.8125, 1.625, 1.625, 60),
(1, 51, 1, 1, 1, 51);

-- --------------------------------------------------------

--
-- Table structure for table `hospital_rating_bd`
--

CREATE TABLE `hospital_rating_bd` (
  `id` int(11) NOT NULL,
  `question1` float NOT NULL,
  `question2` float NOT NULL,
  `question3` float NOT NULL,
  `question4` float NOT NULL,
  `question5` float NOT NULL,
  `question6` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hospital_rating_bd`
--

INSERT INTO `hospital_rating_bd` (`id`, `question1`, `question2`, `question3`, `question4`, `question5`, `question6`) VALUES
(5, 0, 0, 0, 0, 0, 50),
(4, 0, 0, 0, 0, 0, 50),
(3, 1.5, 1, 1, 1, 1, 51),
(2, 0, 0, 0, 0, 0, 50),
(1, 1, 1, 1, 1, 1, 51);

-- --------------------------------------------------------

--
-- Table structure for table `hospital_rating_doctor`
--

CREATE TABLE `hospital_rating_doctor` (
  `id` int(11) NOT NULL,
  `question1` int(11) NOT NULL,
  `question2` float NOT NULL,
  `question3` float NOT NULL,
  `question4` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hospital_rating_doctor`
--

INSERT INTO `hospital_rating_doctor` (`id`, `question1`, `question2`, `question3`, `question4`) VALUES
(1, 26, 1, 1, 51),
(2, 50, 0, 0, 50),
(3, 26, 1, 1, 51),
(4, 50, 0, 0, 50),
(5, 50, 0, 0, 50);

-- --------------------------------------------------------

--
-- Table structure for table `hospital_rating_facility`
--

CREATE TABLE `hospital_rating_facility` (
  `id` int(11) NOT NULL,
  `question1` float NOT NULL,
  `question2` float NOT NULL,
  `question3` float NOT NULL,
  `question4` float NOT NULL,
  `question5` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hospital_rating_facility`
--

INSERT INTO `hospital_rating_facility` (`id`, `question1`, `question2`, `question3`, `question4`, `question5`) VALUES
(5, 0, 0, 0, 0, 50),
(4, 0, 0, 0, 0, 50),
(3, 1, 1, 1, 1, 51),
(2, 0, 0, 0, 0, 50),
(1, 1, 1, 1, 1, 51);

-- --------------------------------------------------------

--
-- Table structure for table `hospital_rating_nursing`
--

CREATE TABLE `hospital_rating_nursing` (
  `id` int(11) NOT NULL,
  `question1` float NOT NULL,
  `question2` float NOT NULL,
  `question3` float NOT NULL,
  `question4` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hospital_rating_nursing`
--

INSERT INTO `hospital_rating_nursing` (`id`, `question1`, `question2`, `question3`, `question4`) VALUES
(1, 1, 1, 1, 51),
(2, 0, 0, 0, 50),
(3, 1, 1, 1, 51),
(4, 0, 0, 0, 50),
(5, 0, 0, 0, 50);

-- --------------------------------------------------------

--
-- Table structure for table `hospital_rating_services`
--

CREATE TABLE `hospital_rating_services` (
  `id` int(11) NOT NULL,
  `question1` float NOT NULL,
  `question2` float NOT NULL,
  `question3` float NOT NULL,
  `question4` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hospital_rating_services`
--

INSERT INTO `hospital_rating_services` (`id`, `question1`, `question2`, `question3`, `question4`) VALUES
(5, 0, 0, 0, 50),
(4, 0, 0, 0, 50),
(3, 1, 1, 1, 51),
(2, 0, 0, 0, 50),
(1, 1, 1, 1, 51);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `hospital_details`
--
ALTER TABLE `hospital_details`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `hospital_rating`
--
ALTER TABLE `hospital_rating`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `hospital_rating_nursing`
--
ALTER TABLE `hospital_rating_nursing`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
