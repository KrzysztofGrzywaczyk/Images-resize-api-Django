This is an rest API app, that allows any user to upload an image in PNG or JPG format.

There are three bultin account tiers: **Basic, Premium and Enterprise**

- users are created via the graphic admin interface panel:

**/admin/**

- login user is able to list his uploded images:

**GET api/images/**

- login users are able to upload an images via HTTP request:

**POST api/images/**

Client should post:

- name : name of the image

- image: image in .jpg or .png format

in response:

- Basic Users will get: a link to a thumbnail that's 200px in height

- Premium Users : a link to a thumbnail that's 200px in height, 400px in height and originally uploaded image

- Enterprise Users: a link to a thumbnail that's 200px in height, 400px in height and originally uploaded image

- Enterprise Users have an ability to create a link object to the original image with time of expiring attached, based on given time in seconds:

**POST /api/links/\<id\_of\_image\>**

(it is possible to check user's images by -\> _GET /images/_ request )

**User should post in json format:**

- img: id of image

-expires\_at: seconds of validation time

**In response user get :**

- a link to original image

- counted time and date at which link should be expired based on given amount of time

Unfortunately I was not be able to perform ability for admins to create arbitrary tiers with things configurable and performance considerations.

But I enclose:

- simple tests with pytest and unittest

- docker and docker compose files as a way to set up the project

- git repository

  

Time of work: 4 sessions about 4-5 hour-long each.



Some example users of each tier have been added.

basicuser, premiumuser and enterpriseuser - their password: Password!123
