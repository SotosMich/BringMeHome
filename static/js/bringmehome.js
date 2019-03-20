// Define the current page
var page;
function setPage(page) {
    this.page = page;
}

// Function for Confirmation button
// It is used for save/delete profile
function JSalert(form) {
    if (form.id == 'save') {
        swal({
            title: "Modifications",
            text: "Are you sure that you want to make these changes on your profile?",
            icon: "warning",
            buttons: true,
            dangerMode: true,
        })
            .then((willDelete) => {
                if (willDelete) {
                    swal("Your personal infomration has been changed!", {
                        icon: "success",
                    }).then(function () {
                        form.submit(); // <--- submit form programmatically
                    });
                } else {
                    swal("Changes discarded!").then(function () {
                        return false; // <--- submit form programmatically
                    });
                }
            });
    } else if (form.id == 'deletion') {
        swal({
            title: "Deletion",
            text: "Once deleted, you will not be able to log in!",
            icon: "warning",
            buttons: true,
            dangerMode: true,
        })
            .then((willDelete) => {
                if (willDelete) {
                    swal("You are account has been deleted! Thank you for being a member so far. We hope to see you soon!", {
                        icon: "success",
                    }).then(function () {
                        form.submit(); // <--- submit form programmatically
                    });
                } else {
                    swal("Deletion discarded!").then(function () {
                        return false; // <--- submit form programmatically
                    });
                }
            });
    }

}


// Map Initialization
function initMap() {
    if (page == 'profile') {
        var location_input = document.getElementById('id_location');
        var autocomplete = new google.maps.places.Autocomplete(location_input);
    } else {
        if (page == 'add') {
            var location_input = document.getElementById('id_location');
            var autocomplete = new google.maps.places.Autocomplete(location_input);
            var address = "Glasgow";
        } else {
            // enters in case of show post
            var address = (document.getElementById('id_location')).innerHTML;
        }
        var geocoder = new google.maps.Geocoder();
        var map = new google.maps.Map(document.getElementById('googleMap'), {
            zoom: 15,
            scrollwheel: true,
        });

        var infowindow = new google.maps.InfoWindow({
            content: address
        });

        geocoder.geocode({ 'address': address }, function (results, status) {
            if (status === 'OK') {
                map.setCenter(results[0].geometry.location);
                var marker = new google.maps.Marker({
                    map: map,
                    position: results[0].geometry.location,
                    title: results[0].address
                });
            } else {
                alert('Geocode was not successful for the following reason: ' + status);
            }
            // Attach it to the marker we've just added
            google.maps.event.addListener(marker, 'click', function () {
                infowindow.open(map, marker);
            })
        })
    }

}

function change_address(address) {
    var address = address;
    var geocoder = new google.maps.Geocoder();
    var map = new google.maps.Map(document.getElementById('googleMap'), {
        zoom: 15,
        scrollwheel: true,
    });

    geocoder.geocode({ 'address': address }, function (results, status) {
        if (status === 'OK') {
            map.setCenter(results[0].geometry.location);
            var marker = new google.maps.Marker({
                map: map,
                position: results[0].geometry.location
            });
        } else {
            alert('Geocode was not successful for the following reason: ' + status);
        }
    })
}