<!-- PROJECT LOGO -->

<h1 align="center">
 Oracle and Grafana integration without plugins
</h1>

<!-- PROJECT SHIELDS -->
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<p>
Project to integrate the Oracle database with Grafana without using plugins.&nbsp<br>
</p>
<p>
Simple execution like 1, 2, 3
</p>
  
   1. Build your Oracle query<br>
   2. Python script to execute the Oracle query and put the result inside Influx<br>
   3. Grafana reads Influx data<br>

 


<!-- TABLE OF CONTENTS -->
## Table of Contents

* [Technologies](#technologies)
* [Getting Started](#getting-started)
  * [Installation](#installation)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)


<!-- ABOUT THE PROJECT -->

## Technologies
* [Python](https://www.python.org/) <img src="https://github.com/marcosmarcon/Oracle-and-Grafana-integration/blob/master/images/python.svg" alt="Logo" width="30" height="30">
  
* [InfluxDB](https://www.influxdata.com/) <img src="https://github.com/marcosmarcon/Oracle-and-Grafana-integration/blob/master/images/influx.svg" alt="Logo" width="30" height="30">
  
* [Grafana](https://grafana.com/) <img src="https://github.com/marcosmarcon/Oracle-and-Grafana-integration/blob/master/images/grafana.svg" alt="Logo" width="30" height="30">


<!-- GETTING STARTED -->
## Getting Started

First it is necessary to install Python and Python library cx_Oracle.
### Installation

1. Clone the repo
```sh
git clone https://github.com/marcosmarcon/Oracle-and-Grafana-integration
```
2. Install packages
```sh
python -m pip install cx_Oracle --upgrade pip
```

<!-- CONTRIBUTING -->
## Contributing

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/Feature`)
3. Commit your Changes (`git commit -m 'Add some Feature'`)
4. Push to the Branch (`git push origin feature/Feature`)
5. Open a Pull Request


<!-- LICENSE -->
## License
Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact
Project Link: [https://github.com/marcosmarcon/Oracle-and-Grafana-integration](https://github.com/marcosmarcon/Oracle-and-Grafana-integration)

Linkedin: [https://www.linkedin.com/in/marcos-marcon-048a7855/](https://www.linkedin.com/in/marcos-marcon-048a7855/)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[license-shield]: https://img.shields.io/badge/License-MIT-blue.svg
[license-url]: https://opensource.org/licenses/MIT
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: linkedin.com/in/marcos-marcon-048a7855
