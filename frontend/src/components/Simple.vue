<template>
  <div class="Simple">
    <div id="top_div" style="height: 60%">
      <v-map :zoom="zoom" :center="center" style="height: 400px; width: 800px">
        <v-tilelayer :url="url" :attribution="attribution"></v-tilelayer>
        <v-marker :lat-lng="marker"></v-marker>
      </v-map>
    </div>
  </div>
</template>

<script>
import Vue2Leaflet from 'vue2-leaflet'

export default {
  name: 'Simple',
  components: {
    'v-map': Vue2Leaflet.Map,
    'v-tilelayer': Vue2Leaflet.TileLayer,
    'v-marker': Vue2Leaflet.Marker
  },
  data () {
    return {
      zoom: 13,
      center: [34.259464, 108.946982],
      url: 'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
      attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      marker: [34.259464, 108.946982]
    }
  }
}
</script>

<style>
@import "../../node_modules/leaflet/dist/leaflet.css";

</style>
