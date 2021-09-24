import HomePage from "../components/HomePage";
import IRoute from "../interfaces/IRoute";
import Debg from "../components/Debg"

const routes: IRoute[] = [
    {
        path: '/',
        name: 'Home page',
        component: HomePage,
        exact: true
    },
    {
        path: '/dbg',
        name: 'Debug page',
        component: Debg,
        exact: true
    }
];
export default routes;