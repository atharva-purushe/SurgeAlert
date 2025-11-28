import React from "react";
import { useNavigate } from "react-router-dom";
import { SignedIn, SignedOut, UserButton } from "@clerk/clerk-react";

export default function Navbar() {
  const navigate = useNavigate();

  return (
    <nav className="w-full border-b border-border bg-card/80 backdrop-blur-md sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
        <h1
          className="text-xl font-bold tracking-tight text-primary cursor-pointer"
          onClick={() => navigate("/")}
        >
          SurgeShield AI
        </h1>

        <div className="flex items-center gap-4">
          {/* Dashboard Button */}
          <button
            className="px-4 py-2 rounded-md border border-border hover:bg-muted transition"
            onClick={() => navigate("/dashboard")}
          >
            Dashboard
          </button>

          {/* Show Login when signed out */}
          <SignedOut>
            <button
              onClick={() => navigate("/sign-in")}
              className="px-4 py-2 rounded-md bg-primary text-primary-foreground hover:opacity-90 transition"
            >
              Login
            </button>
          </SignedOut>

          {/* User Profile Button when logged in */}
          <SignedIn>
            <UserButton afterSignOutUrl="/" />
          </SignedIn>
        </div>
      </div>
    </nav>
  );
}
