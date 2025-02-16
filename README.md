# SkyscannerReferrals Python SDK 1.0.0

Welcome to the SkyscannerReferrals SDK documentation. This guide will help you get started with integrating and using the SkyscannerReferrals SDK in your project.

## Versions

- API version: `1.0.0`
- SDK version: `1.0.0`

## Table of Contents

- [Setup & Configuration](#setup--configuration)
  - [Supported Language Versions](#supported-language-versions)
  - [Installation](#installation)
- [Authentication](#authentication)
  - [API Key Authentication](#api-key-authentication)
- [Services](#services)
- [Models](#models)
- [License](#license)

## Setup & Configuration

### Supported Language Versions

This SDK is compatible with the following versions: `Python >= 3.7`

### Installation

To get started with the SDK, we recommend installing using `pip`:

```bash
pip install skyscanner-referrals
```

## Authentication

### API Key Authentication

The SkyscannerReferrals API uses API keys as a form of authentication. An API key is a unique identifier used to authenticate a user, developer, or a program that is calling the API.

#### Setting the API key

When you initialize the SDK, you can set the API key as follows:

```py
SkyscannerReferrals(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER"
)
```

If you need to set or update the API key after initializing the SDK, you can use:

```py
sdk.set_api_key("YOUR_API_KEY", "YOUR_API_KEY_HEADER")
```

## Services

The SDK provides various services to interact with the API.

<details> 
<summary>Below is a list of all available services with links to their detailed documentation:</summary>

| Name                                                       |
| :--------------------------------------------------------- |
| [FlightsService](documentation/services/FlightsService.md) |
| [HotelsService](documentation/services/HotelsService.md)   |
| [CarHireService](documentation/services/CarHireService.md) |

</details>

## License

This SDK is licensed under the MIT License.

See the [LICENSE](LICENSE) file for more details.

<!-- This file was generated by liblab | https://liblab.com/ -->
