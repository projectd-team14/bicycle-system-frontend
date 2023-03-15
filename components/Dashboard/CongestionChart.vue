<template>
    <v-card
        class="mx-auto box"
        max-height="420"
        style="background: linear-gradient(#14F3FF, #6E00B2);"
    > 
        <v-card-item>
            <v-card-title class="headline">混雑度</v-card-title>
            <div
                class="justify-center"
                style="height: 350px;"
            >
                <v-col
                    cols="12"
                    class="d-flex justify-center"
                    v-for="(spots, i) in $store.state.homeData.homeData"
                    :key="i"
                >
                    <v-progress-circular
                        :size="180"
                        :width="10"
                        :value="100 * spots.count / spots.max"
                        :color="spots.border_color"
                        :styles="chartStyles"
                    >
                        <h2>{{ 100 * spots.count / spots.max }}%</h2>
                    </v-progress-circular>
                </v-col>
            </div>
        </v-card-item>
    </v-card>            
</template>
  
<script>
export default {
    data() {
        return{
            height: 100
        }
    },
    computed:{
        chartStyles() {
            return{
                height: `${this.height}%`,
                position:'relative'
            }
        }
    }
}
</script>

<style scoped>
.box {
    overflow-y: scroll;
    -ms-overflow-style: none;
    scrollbar-width: none;
}

.box::-webkit-scrollbar {
    display:none;
}
</style>