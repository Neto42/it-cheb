<template>
  <div class="hello">
    <yandex-map
        zoom="10"
        style="width: 100%; max-width: 100%; height: 98vh;"
        :coords="coords"
        @map-was-initialized="mapInit"
    >
      <ymap-marker
          v-for="billboard in allResults"
          marker-type="placemark"
          :balloon-template="mapBalloon(billboard)"
          :coords="billboard.coords"
          :marker-id="index"
          :icon="{ color: 'blue' }"
          :key="billboard.id"
      ></ymap-marker>
    </yandex-map>
  </div>
</template>

<script>
/* eslint-disable */
import {yandexMap, ymapMarker} from "vue-yandex-maps";
import {mapActions, mapGetters} from "vuex";

export default {
  name: "HelloWorld",
  components: {yandexMap, ymapMarker},
  data() {
    return {
      coords: [56.1322200, 47.2519400],
      mapLoaded: false,
      options: {
        layout: "default#image",
        imageSize: [30, 40],
        contentOffset: [0, 0]
      },
    };
  },
  computed: mapGetters(['allResults']),
  mounted() {
    this.results('network/rezult/')
  },
  methods: {
    ...mapActions(['results']),

    mapInit(map) {
      this.mapLoaded = true;
      this.map = map;
      addresses.map(address => {
            ymaps.geocode(address.address, {
        results: 1
    }).then(function (res) {
            // Выбираем первый результат геокодирования.
            var firstGeoObject = res.geoObjects.get(0);
                // Координаты геообъекта.
                // Область видимости геообъекта.

            firstGeoObject.options.set('preset', 'islands#darkOrangeDotIconWithCaption');
            // Получаем строку с адресом и выводим в иконке геообъекта.
            firstGeoObject.properties.set('iconCaption', firstGeoObject.getAddressLine());

            // Добавляем первый найденный геообъект на карту.
            map.geoObjects.add(firstGeoObject);
            // Масштабируем карту на область видимости геообъекта.
        });
      })
    },
    mapBalloon(billboard) {
      return `
      <div><h1>${billboard.id}</h1>
      <p><strong>Адрес</strong>: ${billboard.street}</p>
      </div>
      `;
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0;
}

a {
  color: #42b983;
}
</style>