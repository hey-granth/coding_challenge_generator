import ClerkProviderWithRoutes from './auth/ClerkProviderWithRoutes.jsx'
import {Routes, Route} from 'react-router-dom'
import './App.css'
import {Layout} from "./layout/Layout.jsx";
import {HistoryPanel} from "./history/HistoryPanel.jsx"
import {AuthenticationPage} from "./auth/AuthenticationPage.jsx"
import {ChallengeGenerator} from "./challenge/ChallengeGenerator.jsx";

function App() {
    return <ClerkProviderWithRoutes>
        <Routes>
            <Route path="/sign-in/*" element={<AuthenticationPage mode="sign-in" />} />
            <Route path="/sign-up/" element={<AuthenticationPage mode="sign-up" />} />
            <Route element={<Layout />} >
                <Route path="/" element={<ChallengeGenerator />} />
                <Route path="/history" element={<HistoryPanel />} />
            </Route>
        </Routes>
    </ClerkProviderWithRoutes>
}

export default App
