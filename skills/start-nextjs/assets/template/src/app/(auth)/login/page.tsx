import type { Metadata } from "next";

export const metadata: Metadata = { title: "Login" };

export default function LoginPage() {
  return (
    <main id="main-content" tabIndex={-1} className="grid flex-1 place-items-center p-6">
      <h1>Login</h1>
    </main>
  );
}
