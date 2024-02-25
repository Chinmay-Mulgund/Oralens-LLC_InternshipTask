# Multipara Monitor Data Interpretation

This project aims to develop software for interpreting data from multipara monitors using a video feed. The software is designed to be adaptable across different monitor models.

## Table of Contents

- [Introduction](#introduction)
- [Objectives](#objectives)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Usage](#usage)
- [Project Structure](#project-structure)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project focuses on developing a software solution to interpret data from multipara monitors via video feed. It consists of two main tasks: detecting data display areas and extracting numeric values using Optical Character Recognition (OCR).

## Objectives

1. **Task 1: Detection of Data Display Areas**
   - Identify critical data areas (e.g., Heart Rate, ECG, Oxygen Levels) on varying monitor screens.

2. **Task 2: Detection of Displayed Values**
   - Use OCR to digitize numeric values of Heart Rate and Oxygen Saturation from the identified areas.

## Features

- Interactive selection of Region of Interest (ROI) from video feed.
- Full-screen display of the video.
- OCR-based extraction of numeric values from the selected ROI.

## Getting Started

### Installation

1. Clone the repository to your local machine.

   ```bash
   git clone https://github.com/your-username/multipara-monitor-interpreter.git
