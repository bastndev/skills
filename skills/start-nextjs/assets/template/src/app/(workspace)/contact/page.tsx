import type { Metadata } from "next";
import GXB from "@/src/components/ui/GXB";

export const metadata: Metadata = { title: "Contact" };

export default function ContactPage() {
  return (
    <main id="main-content" tabIndex={-1} className="flex flex-1">
      <h1 className="sr-only">Contact</h1>
      <GXB text="Contact — get in touch or drop your details here." />
    </main>
  );
}
