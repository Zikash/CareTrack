import { createStore } from "vuex"; 

export default createStore({
    state: {
        patient: null,
        doctor: null,
        administator: null,
        Auth: false
    },
    getters: {
        isAuth(state) {
            if (state.patient != null || state.doctor != null || state.administator != null){
                return true
            }
            return false
        }
    },
    mutations: {
        updatePatient(state, patient) {
            state.patient = patient
        },
        updateDoctor(state, doctor){
            state.doctor = doctor
        },
        updateAdministator(state, administator){
            state.administator = administator
        }
    }
})