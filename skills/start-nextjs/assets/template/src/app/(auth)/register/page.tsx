import type { Metadata } from "next";

export const metadata: Metadata = { title: "Register" };

export default function RegisterPage() {
  return (
    <main id="main-content" tabIndex={-1} className="grid flex-1 place-items-center p-6">
      <h1>Register</h1>
    </main>
  );
}
