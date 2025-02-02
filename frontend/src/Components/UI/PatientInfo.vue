<template>
            <div class="main">
                <div class="headbar">
                    <h2 
                    @click="infoPage = 'patient'" 
                    class="name profile" 
                    :class="{
                        thenPage: infoPage === 'patient'
                    }">Пациент</h2>

                    <h2
                    @click="infoPage = 'osmotrs'" 
                    class="name osmotrs" 
                    :class="{
                        'thenPage': infoPage === 'osmotrs' || infoPage === 'osmotr'
                    }">Осмотры</h2>
                </div>
                
            
                <div class="main__view">

                    <div class="patient_profile" v-if="infoPage === 'patient'">

                    </div>
                        
                    <div class="patient_osmotrs" v-else-if="infoPage === 'osmotrs'">
                        <osmotr-bar 
                        v-for="osmotr in osmotrs" 
                        :osmotr="osmotr"/>
                    </div>
                    <div class="patient_osmotr" v-else-if="infoPage === 'osmotr'">

                    </div>

                        

                </div>
                    
            </div>

</template>

<script>

    export default {
        name: 'patient-info',
        data() {
            return {
                infoPage: 'patient',
                osmotrs: [
                    {
                        id: 1,
                        doctor: {
                            id: 1,
                            Fio: "Nikolay Pobelov Homonaft",
                            Phone: "8 999 999 99-99",
                            Place: 1,
                            Stage: 1
                        },
                        patient: {
                            id: 1,
                            Fio: "Haruton ebrog Afomon",
                            Phone: "8 888 099 73-89",
                            Address: "moletare 17"
                        },
                        place: "Hospital",
                        Date_this: "11.11.11",
                        Time_this: "11:11"
                    },
                    {
                        id: 2,
                        doctor: {
                            id: 2,
                            Fio: "Nikolay Pobelov Homonaft",
                            Phone: "8 999 988 99-99",
                            Place: 2,
                            Stage: 4
                        },
                        patient: {
                            id: 2,
                            Fio: "Haruton ebrog Afomon",
                            Phone: "8 888 099 73-89",
                            Address: "hoolersire h. 57"
                        },
                        place: "Home",
                        Date_this: "11.11.11",
                        Time_this: "11:66"
                    }
                ]
            }
        }
    }
</script>

<style scoped>

input {
background-color: #F0EEEE;
}

textarea {
background-color: #F0EEEE;
}


form {
display: flex;
margin-left: auto;
margin-right: auto;
}

.main_div {
display:flex;
flex-wrap: wrap;
margin-top: 20px;
margin-left: auto;
margin-right: auto;
min-width: 500px;
}

.main {
margin-top: 20px;
margin-left: auto;
margin-right: auto;
min-width: 500px;
}

.headbar {
display: flex;

}


.name {
background-color: white;
border-radius: 10px 10px 0 0;
align-content: center;
text-align: center;
width: 100%;
padding: 15px;
height: 50px;
}

.profile {
    box-shadow: -3px -3px 4px 3px rgba(34, 60, 80, 0.2) inset;
}

.doctors {
    box-shadow: 0px -2px 4px 3px rgba(34, 60, 80, 0.2) inset;
}

.patients {
    box-shadow: 0px -2px 4px 3px rgba(34, 60, 80, 0.2) inset;
}

.osmotrs {
    box-shadow: 3px -3px 4px 3px rgba(34, 60, 80, 0.2) inset;
}

.thenPage {
    box-shadow: 0px 0px 0px 0px rgba(34, 60, 80, 0.2) inset;
}



.main__view {
background-color: white;
padding: 35px;
margin-left: auto;
margin-right: auto;
border-radius: 0px 10px 10px 10px;
}

.rootBox {
    padding-left: 40px;
    padding-right: 40px;
    margin-bottom: 40px;
}

.root {
    margin-left: auto;
    margin-right: auto;
    text-align: center;
    align-content: center;
    background-color: #D9D9D9;
    height: 40px;
    border-radius: 5px;
}

.content_profile {
    display: flex;
    margin-top: 8px;
    margin-bottom: 15px;
}

.content_profile h3 {
    background-color: #D9D9D9;
    padding: 5px;
    border-radius: 5px;
}

.content_profile button {
    background-color: #69C553;
    border-radius: 5px;
    padding: 5px;
    margin-left: 20px;
}

.exitBox {
    display: flex;
}

.exit {
    background-color: #B83E40;
    border-radius: 5px;
    padding: 8px;
    margin-top: 10px;
    margin-left: auto;
    margin-right: 20px;
}


</style>