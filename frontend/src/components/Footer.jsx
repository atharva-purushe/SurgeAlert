import React from 'react'

const Footer = () => {
  return (
    <footer className="border-t border-border py-6 text-center text-muted-foreground">
        © {new Date().getFullYear()} SurgeShield AI — Autonomous Hospital Surge Management
      </footer>
  )
}

export default Footer