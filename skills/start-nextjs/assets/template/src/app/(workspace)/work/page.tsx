import type { Metadata } from "next";
import GXB from "@/src/components/ui/GXB";

export const metadata: Metadata = { title: "Work" };

export default function WorkPage() {
  return (
    <main id="main-content" tabIndex={-1} className="flex flex-1">
      <h1 className="sr-only">Work</h1>
      <GXB text="Work — a place to showcase your projects." />
    </main>
  );
}
