<template>
    <v-card
        class="mx-auto box"
        max-height="880"
        style="background: #2c2d3f;"
    > 
        <v-card-item>
            <v-card-title class="headline">カメラ</v-card-title>
            <div
                class="justify-center"
                style="height: 790px;"
            >
                <v-list
                    class="item-list box"
                    dense
                    nav
                    style="background: #2c2d3f;"
                >
                    <template v-for="(navigation, i) in this.navigationList">
                        <v-list-group
                            v-if="typeof navigation == 'object'"
                            :key="i"
                            :prepend-icon="navigation.icon"
                        >
                            <template v-slot:activator>
                                <v-list-item-content>
                                <v-list-item-title
                                    class="text-subtitle-1"
                                    v-text="navigation.title"
                                />
                                </v-list-item-content>
                            </template>
                            <v-list-item
                                v-for="(subNavigation, j) in navigation.items"
                                :key="j"
                                :to="subNavigation.to"
                                :exact="subNavigation.exact"
                                @click="onLoadSettingData(navigation.title)"
                            >
                                <v-list-item-icon>
                                    <v-icon>{{ subNavigation.icon }}</v-icon>
                                </v-list-item-icon>
                                <v-list-item-content>
                                    <v-list-item-title
                                        v-text="subNavigation.title"
                                    />
                                </v-list-item-content>
                            </v-list-item>
                        </v-list-group>
                        <v-list-item
                            v-else
                            :key="i"
                            :to="navigation.to"
                            :exact="navigation.exact"
                        >
                            <v-list-item-action>
                                <v-icon>{{ navigation.icon }}</v-icon>
                            </v-list-item-action>
                            <v-list-item-content>
                                <v-list-item-title
                                    class="text-subtitle-1"
                                    v-text="navigation.title"
                                />
                            </v-list-item-content>
                        </v-list-item>
                    </template>            
                </v-list>

            </div>
        </v-card-item>
    </v-card>            
</template>
  
<script>
export default {
    data() {
        return{
            navigationList: [],
            sideNavigationList: [],
            camerasData: [],
            height: 100
        }
    },
    computed: {
        chartStyles() {
            return {
                height: `${this.height}%`,
                position:'relative'
            }
        },
        getCameraData: function() {
            return this.$store.getters["cameraData/getCameraData"];
        }
    },
    watch: {
        getCameraData(values) {
            if (typeof this.camerasData == 'undefined') {
                return this.navigationList;
            }

            this.camerasData = this.$store.state.cameraData.cameraData;
            
            for (let i = 0; i < this.camerasData.length; i++) {
                var data = {
                    icon: "mdi-cctv",
                    title: this.camerasData[i].cameras_name,
                    items: [
                        {
                            icon: "mdi-dip-switch",
                            title: "動作設定",
                            to: "/" + String(this.camerasData[i].cameras_id) + "/cameraSetting",
                            exact: true
                        },
                        {
                            icon: "mdi-image-size-select-large",
                            title: "範囲設定",
                            to: "/" + String(this.camerasData[i].cameras_id) + "/labelSetting",
                            exact: true
                        }
                    ]
                }

                this.navigationList.push(data);
            }
    
            return this.navigationList;
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