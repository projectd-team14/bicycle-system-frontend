<template>
    <v-card
        class="mx-auto"
        max-height="420"
        style="background: #2c2d3f;"
    > 
        <v-card-item>
            <v-card-title class="headline">駐輪場マップ</v-card-title>
            <div style="height: 350px;">
                <GmapMap
                    ref="gmp"
                    map-type-id="roadmap"
                    :center="maplocation"
                    :zoom="zoom"
                    :style="styleMap"
                    :options="mapOptions"
                >
                    <GmapMarker
                        v-for="(m, index) in markers"
                        :key="index"
                        :title="m.title"
                        :position="m.position"
                        :clickable="true"
                        :draggable="false"
                        @click="onClickMarker(index, m)"
                    />
                    <GmapInfoWindow
                        :options="infoOptions"
                        :position="infoWindowPos"
                        :opened="infoWinOpen"
                        @closeclick="infoWinOpen = false"
                    >
                        <p style="color: #000">
                        {{ marker.title }}
                        </p>
                        <iframe
                            width="560"
                            height="315"
                            :src="marker.url"
                            title="YouTube video player" 
                            frameborder="0"
                            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                            allowfullscreen
                        >
                        </iframe>
                    </GmapInfoWindow>
                </GmapMap>
            </div>               
        </v-card-item>
    </v-card>            
</template>
  
<script>
export default {
    data() {
        return {
            height: 100,
            zoom: 9,
            maplocation: {
                lat: 35.6581,
                lng: 139.7017 
            },
            styleMap: {
                width: '100%',
                height: '100%'
            },
            mapOptions: {
                zoomControl: false,
                fullscreenControl: false,
                streetViewControl: false,
                scaleControl: false,
                mapTypeControl: false,
                panControl: false,
                styles: [
                    {
                        "featureType": "all",
                        "elementType": "labels.text.fill",
                        "stylers": [
                            {
                                "color": "#ffffff"
                            }
                        ]
                    },
                    {
                        "featureType": "all",
                        "elementType": "labels.text.stroke",
                        "stylers": [
                            {
                                "color": "#000000"
                            },
                            {
                                "lightness": 13
                            }
                        ]
                    },
                    {
                        "featureType": "administrative",
                        "elementType": "geometry.fill",
                        "stylers": [
                            {
                                "color": "#000000"
                            }
                        ]
                    },
                    {
                        "featureType": "administrative",
                        "elementType": "geometry.stroke",
                        "stylers": [
                            {
                                "color": "#144b53"
                            },
                            {
                                "lightness": 14
                            },
                            {
                                "weight": 1.4
                            }
                        ]
                    },
                    {
                        "featureType": "landscape",
                        "elementType": "all",
                        "stylers": [
                            {
                                "color": "#08304b"
                            }
                        ]
                    },
                    {
                        "featureType": "poi",
                        "elementType": "geometry",
                        "stylers": [
                            {
                                "color": "#0c4152"
                            },
                            {
                                "lightness": 5
                            }
                        ]
                    },
                    {
                        "featureType": "road.highway",
                        "elementType": "geometry.fill",
                        "stylers": [
                            {
                                "color": "#000000"
                            }
                        ]
                    },
                    {
                        "featureType": "road.highway",
                        "elementType": "geometry.stroke",
                        "stylers": [
                            {
                                "color": "#0b434f"
                            },
                            {
                                "lightness": 25
                            }
                        ]
                    },
                    {
                        "featureType": "road.arterial",
                        "elementType": "geometry.fill",
                        "stylers": [
                            {
                                "color": "#000000"
                            }
                        ]
                    },
                    {
                        "featureType": "road.arterial",
                        "elementType": "geometry.stroke",
                        "stylers": [
                            {
                                "color": "#0b3d51"
                            },
                            {
                                "lightness": 16
                            }
                        ]
                    },
                    {
                        "featureType": "road.local",
                        "elementType": "geometry",
                        "stylers": [
                            {
                                "color": "#000000"
                            }
                        ]
                    },
                    {
                        "featureType": "transit",
                        "elementType": "all",
                        "stylers": [
                            {
                                "color": "#146474"
                            }
                        ]
                    },
                    {
                        "featureType": "water",
                        "elementType": "all",
                        "stylers": [
                            {
                                "color": "#021019"
                            }
                        ]
                    }
                ]
            },
            infoOptions: {
                minWidth: 560,
                pixelOffset: {
                    width: 0,
                    height: 0,
                },
            },
            infoWindowPos: null,
            infoWinOpen: false,
            marker: {},
            markers: []
        }
    },
    computed: {
        getHomeData: function() {
            return this.$store.getters["homeData/getHomeData"];
        }
    },
    watch: {
        getHomeData(values) {
            for (let i = 0; i < values.length; i++) {
                var urlReplace = values[i].url.replace('watch?v=', 'embed/');
                const dataset = {
                    title: values[i].name,
                    url: urlReplace,
                    position: {
                        lat: parseFloat(values[i].latitude),
                        lng: parseFloat(values[i].longitude) 
                    }
                }
                this.markers.push(dataset);
            }
        }
    },
    methods: {
    getCurrentPosition() {
      return new Promise(function (resolve, reject) {
        navigator.geolocation.getCurrentPosition(resolve, reject)
      })
    },
    onClickMarker(index, marker) {
      this.$refs.gmp.panTo(marker.position)
      this.infoWindowPos = marker.position
      this.marker = marker
      this.infoWinOpen = true
    },
  },
}
</script>