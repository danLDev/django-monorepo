import { Link } from "@tanstack/react-router";

export default function Header() {
  return (
    <>
      <header className="p-4 flex items-center bg-gray-200 text-white shadow-lg">
        <Link to="/">Stuido Finder</Link>
      </header>
    </>
  )
}
