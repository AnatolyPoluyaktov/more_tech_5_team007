import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Landing, SearchBankBranch } from "../pages";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<Landing />} path="/" />
        <Route element={<Landing />} path="/:people" />
        <Route element={<SearchBankBranch />} path="/search-bank-branch" />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
