<template>
<el-row>
  <p><strong>Leaflet Map<Strong></p>
  <el-card >
    <div id="top_div">
      <v-map :zoom="zoom" :center="center">
        <v-tilelayer :url="url" :attribution="attribution"></v-tilelayer>
        <v-marker v-for="item in markers" :key="item.id" :visible="item.visible" :draggable="item.draggable" :lat-lng="item.position" v-on:l-click="alert(item)"></v-marker>
        <v-icondefault :image-path="path"></v-icondefault>
      </v-map>
    </div>
  </el-card>
  <p>Markers related action</p>
  <div style="height: 50">
    <button name="button" v-on:click="addMarkers">Add Markers</button>
    <button name="button" v-on:click="removeMarkers">Remove Markers</button>
    <button name="button" v-on:click="requestTestString">Request Data</button>
  </div>
</el-row>
</template>

<script src="js/vue.js"></script>
<script src="js/vue-resource.js"></script>
<script>
import Vue from 'vue'
import VueResource from 'vue-resource'
import Vue2Leaflet from 'vue2-leaflet'
Vue.use(VueResource);

// [34.259464, 108.946982]
// L.latLng(31.2304, 121.4737),
export default {
  name: 'LeafletMap',
  components: {
    'v-map': Vue2Leaflet.Map,
    'v-tilelayer': Vue2Leaflet.TileLayer,
    'v-marker': Vue2Leaflet.Marker,
    'v-icondefault': Vue2Leaflet.IconDefault
  },
  data () {
    return {
      zoom: 10,
      path: '/static/images/',
      center: [34.259464, 108.946982],
      url: 'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
      attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      markers: [
        {id: 'm1', position: {lat: 34.259464, lng: 108.946982}, draggable: true, visible: true},
        {id: 'm2', position: {lat: 34.27, lng: 108.95}, draggable: true, visible: true},
        {id: 'm3', position: {lat: 34.25, lng: 108.94}, draggable: true, visible: true},
        {id: 'm4', position: {lat: 34.26, lng: 108.84}, draggable: true, visible: true}
      ],
    }
  },
  methods: {
    alert (item) {
      alert('this is ' + JSON.stringify(item))
    },
    removeMarker: function (index) {
      this.markers.splice(index, 1)
    },
    removeMarkers: function () {
      this.markers = []
    },
    addMarkers: function () {
      this.markers = [
        {id: 'm1', position: {lat: 34.259464, lng: 108.946982}, draggable: true, visible: true},
        {id: 'm2', position: {lat: 34.27, lng: 108.95}, draggable: true, visible: true},
        {id: 'm3', position: {lat: 34.25, lng: 108.94}, draggable: true, visible: true},
        {id: 'm4', position: {lat: 34.26, lng: 108.84}, draggable: true, visible: true}
      ]
    },
    requestTestData: function () {
      // GET /someUrl
      Vue.http.get('http://localhost:2020/api/testdata/').then(response => {
        console.log('result....')
        console.log(response)
        this.markers = response.body
      }, response => {
        // error callback
      })
    },
    requestTestString: function () {
      // GET /someUrl
      Vue.http.get('http://localhost:2020/api/teststring/').then(response => {
        console.log(response)
        // get body data
      }, response => {
        // error callback
      })
    }
  }
}
</script>

<style>
.leaflet-fake-icon-image-2x {
  background-image: url(../../node_modules/leaflet/dist/images/marker-icon-2x.png);
}
.leaflet-fake-icon-shadow {
  background-image: url(../../node_modules/leaflet/dist/images/marker-shadow.png);
}
@import "../../node_modules/leaflet/dist/leaflet.css";

#top_div {
  overflow-x: auto;
  top: 0;
  right: 0;
  left: 0;
  bottom: 0;
  height: 400px;
  width: 100%
}

</style>
