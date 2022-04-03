
<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GPL-3.0 License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/adityash4rma/doodstream_api">
    <img src="https://telegra.ph/file/f4c81a1ac75944b77fe60.png" alt="Logo">
  </a>

<h3 align="center">Doodstream API wrapper</h3>

  <p align="center">
    This is an un-official Doodstream python API Wrapper is just an upgrade or what you can say an maintained fork of <a href="https://github.com/wahyubiman/DoodStream"> THIS! </a>
    <br />
    <a href="https://github.com/adityash4rma/doodstream_api"></a>
    <br />
    <br />
    <a href="https://github.com/adityash4rma/doodstream_api/issues">Report Bug</a>
    ·
    <a href="https://github.com/adityash4rma/doodstream_api/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#Usage">Usage</a></li>
    <li><a href="#todo">TODO</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#donations">Contact</a></li>
  </ol>
</details>


---
<!-- ABOUT THE PROJECT -->
## About The Project 🤔

This API Wrapper is an unofficial python wrapper for the <a href="https://doodstream.com/api-docs"> doodstream API</a>. What is DoodStream? DoodStream is a profitable video hosting service where you can upload, share, and view videos and listen to audios online. It is said that you can get paid for the tasks assigned on this website such as uploading and sharing videos or referring.

<p align="right">(<a href="#top">↥ back to top</a>)</p>


---
<!-- GETTING STARTED -->
## Getting Started 🏃‍♂️

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

---
### Installation 🛠


```sh
pip install doodstream_api
```

<p align="right">(<a href="#top">↥ back to top</a>)</p>

---

### Usage 💡

**Use it as Python Module**
```python
from doodstream_api import doodstream_conf


ds = doodstream_conf('23JC3hcvxxxxxxxxx')


# Check doodstream account info
ds.account_info()

# Check doodstream account reports
ds.account_reports()

# Check DMCA reports for Videos
ds.account_dmca()

# Upload video file from local storage
ds.local_upload("PATH_TO_YOUR_VIDEO")

# Copy/Clone Video to your account
ds.copy_video("FILE_ID")

# Upload video from direct links
ds.remote_upload("DIRECT_VIDEO_LINK")

# Get list & status of remote uploads (errors, current uploads, etc.)
ds.remote_upload_list()

# Get only status of remote uploads
ds.remote_upload_status()

# Info for slots in remote upload
ds.remote_upload_slots()

# Perform Various Action on remote upload
ds.remote_upload_action()

# Create new folder
ds.folder_create('FOLDER_NAME')

# Rename folders
ds.folder_rename('FOLDER_ID','FOLDER_NAME')

# List Files in your Doodstream Account
ds.file_list()

# Specific file status
ds.file_status('FOLDER_ID')

# Get basic file info
ds.file_info("FILE_ID")

# Get file image
ds.file_image('FILE_ID')

# Specific File rename
ds.file_rename('FILE_ID', 'NEW_FILE_NAME')

# Search videos in your Doodstream account
d.file_search("YOUR_KEYWORD")

```

---

<!-- ROADMAP -->
## TODO 👷‍♂️

- [ ] Doodstream CLI
- [ ] Handle more exceptions!



See the [open issues](https://github.com/adityash4rma/doodstream_api/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">↥ back to top</a>)</p>

---

<!-- LICENSE -->
## License 📃

Distributed under the MIT License. See [LICENSE.txt](https://github.com/adityash4rma/doodstream_api/blob/main/LICENSE)  for more information.

<p align="right">(<a href="#top">↥ back to top</a>)</p>


---
<!-- CONTACT -->
## Donations 😃

<a href="https://www.buymeacoffee.com/adityash4rma" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-blue.png" alt="Buy Me A Coffee" height="41" width="174"></a>


<p align="right">(<a href="#top">↥ back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/adityash4rma/doodstream.svg?style=for-the-badge
[contributors-url]: https://github.com/adityash4rma/doodstream_api/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/adityash4rma/doodstream.svg?style=for-the-badge
[forks-url]: https://github.com/adityash4rma/doodstream_api/network/members
[stars-shield]: https://img.shields.io/github/stars/adityash4rma/doodstream.svg?style=for-the-badge
[stars-url]: https://github.com/adityash4rma/doodstream_api/stargazers
[issues-shield]: https://img.shields.io/github/issues/adityash4rma/doodstream.svg?style=for-the-badge
[issues-url]: https://github.com/adityash4rma/doodstream_api/issues
[license-shield]: https://img.shields.io/github/license/adityash4rma/doodstream.svg?style=for-the-badge
[license-url]: https://github.com/adityash4rma/doodstream_api/blob/master/LICENSE
[product-screenshot]: images/screenshot.png
