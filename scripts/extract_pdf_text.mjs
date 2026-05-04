import fs from "node:fs/promises";
import path from "node:path";
import { pathToFileURL } from "node:url";

const pdfjsPath = "C:/Users/gakum/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/pdfjs-dist/legacy/build/pdf.mjs";
const pdfjs = await import(pathToFileURL(pdfjsPath).href);

const input = process.argv[2];
const output = process.argv[3];

if (!input || !output) {
  console.error("Usage: node extract_pdf_text.mjs input.pdf output.txt");
  process.exit(1);
}

const data = new Uint8Array(await fs.readFile(input));
const doc = await pdfjs.getDocument({ data, useWorkerFetch: false, isEvalSupported: false, disableFontFace: true }).promise;

const pages = [];
for (let pageNo = 1; pageNo <= doc.numPages; pageNo += 1) {
  const page = await doc.getPage(pageNo);
  const textContent = await page.getTextContent();
  const lines = [];
  let currentY = null;
  let currentLine = [];

  for (const item of textContent.items) {
    const y = Math.round(item.transform[5]);
    if (currentY === null || Math.abs(y - currentY) <= 2) {
      currentLine.push(item.str);
      currentY = y;
    } else {
      lines.push(currentLine.join("").replace(/\s+/g, " ").trim());
      currentLine = [item.str];
      currentY = y;
    }
  }
  if (currentLine.length) {
    lines.push(currentLine.join("").replace(/\s+/g, " ").trim());
  }

  pages.push(`<!-- page: ${pageNo} -->\n${lines.filter(Boolean).join("\n")}`);
}

await fs.mkdir(path.dirname(output), { recursive: true });
await fs.writeFile(output, pages.join("\n\n"), "utf8");
