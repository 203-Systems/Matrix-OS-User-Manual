# Define source and build directories
SRCDIR := $(subst /,\,$(CURDIR))
BUILDDIR := $(subst \Source\,\PDF\,$(SRCDIR))

# Find all the .md files under the source directory
SRCS := $(shell dir /s /b $(SRCDIR)\*.md)

# Generate PDF paths for each source file
PDFS := $(patsubst $(SRCDIR)%.md,$(BUILDDIR)%.pdf,$(SRCS))

$(info $(SRCDIR))
$(info $(BUILDDIR))
$(info SRCS: $(SRCS))
$(info PDFS: $(PDFS))

# Rule to build all PDFs
all: $(PDFS)

# Rule to build a PDF from a source file
$(BUILDDIR)%.pdf: $(SRCDIR)%.md
	@if not exist $(dir $@) (mkdir $(dir $@))
	@echo Building $@ from $<
	@pandoc $< -o $@ --from markdown --template "../../Template/eisvogel.tex" --listings

# Clean rule to remove all PDFs
clean:
	@echo Cleaning $(BUILDDIR)
	@rm -rf $(BUILDDIR)*.pdf
